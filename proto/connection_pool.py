import asyncio
import time
import logging
from collections import defaultdict

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('ConnectionPool')

class ConnectionPool:
    """异步连接池，管理多个网络连接"""
    
    def __init__(self, max_connections=1000, timeout=60):
        self.max_connections = max_connections
        self.timeout = timeout
        self.connections = {}  # client_id -> connection
        self.last_activity = {}  # client_id -> timestamp
        self.locks = defaultdict(asyncio.Lock)
        self.total_created = 0
        self.total_closed = 0
        
    async def get_connection(self, client_id):
        """获取连接"""
        async with self.locks[client_id]:
            if client_id in self.connections:
                # 更新最后活动时间
                self.last_activity[client_id] = time.time()
                return self.connections[client_id]
            return None
        
    async def add_connection(self, client_id, connection):
        """添加新连接"""
        async with self.locks[client_id]:
            # 检查是否超过最大连接数
            if len(self.connections) >= self.max_connections:
                # 清理超时连接
                await self._cleanup_inactive()
                
                # 如果仍然超过最大连接数，拒绝新连接
                if len(self.connections) >= self.max_connections:
                    logger.warning(f"拒绝连接 {client_id}: 已达到最大连接数 {self.max_connections}")
                    return False
                    
            self.connections[client_id] = connection
            self.last_activity[client_id] = time.time()
            self.total_created += 1
            logger.debug(f"添加新连接: {client_id}, 当前连接数: {len(self.connections)}")
            return True
            
    async def remove_connection(self, client_id):
        """移除连接"""
        async with self.locks[client_id]:
            if client_id in self.connections:
                logger.debug(f"移除连接: {client_id}")
                del self.connections[client_id]
                self.total_closed += 1
                
            if client_id in self.last_activity:
                del self.last_activity[client_id]
                
    async def _cleanup_inactive(self):
        """清理不活跃的连接"""
        now = time.time()
        inactive = []
        
        for client_id, last_time in self.last_activity.items():
            if now - last_time > self.timeout:
                inactive.append(client_id)
                
        if inactive:
            logger.info(f"清理 {len(inactive)} 个不活跃连接")
                
        for client_id in inactive:
            await self.remove_connection(client_id)
            
    def get_stats(self):
        """获取连接池统计信息"""
        return {
            'current_connections': len(self.connections),
            'max_connections': self.max_connections,
            'total_created': self.total_created,
            'total_closed': self.total_closed
        }
        
    async def close_all(self):
        """关闭所有连接"""
        close_tasks = []
        
        # 复制连接列表，避免在迭代时修改
        connections = list(self.connections.items())
        
        for client_id, connection in connections:
            if hasattr(connection, 'close') and callable(connection.close):
                close_tasks.append(self.remove_connection(client_id))
                # 如果 close 是异步函数
                if asyncio.iscoroutinefunction(connection.close):
                    close_tasks.append(connection.close())
                else:
                    connection.close()
                    
        if close_tasks:
            await asyncio.gather(*close_tasks, return_exceptions=True)
            
        logger.info(f"已关闭所有连接: {len(connections)} 个") 