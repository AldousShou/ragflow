# from dataclasses import dataclass
# from functools import wraps
# import pymysql
# # logger.py
# import functools
# import logging
# import mysql.connector
# from typing import Union, List, Optional, Dict
#
# logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
#
# @dataclass
# class SearchResult:
#     total: int
#     ids: List[str]
#     query_vector: List[float] = None
#     field: Optional[Dict] = None
#     highlight: Optional[Dict] = None
#     aggregation: Union[List, Dict, None] = None
#     keywords: Optional[List[str]] = None
#     group_docs: List[List] = None
#
#
# def log_to_mysql(*functions):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             func_name = func.__name__
#             logging.info(f'Function {func_name} called with args: {args}, kwargs: {kwargs}')
#             result = func(*args, **kwargs)
#
#             # Log the function call to MySQL for each registered function
#             for registered_func in functions:
#                 if func_name == registered_func.__name__:
#                     save_log_to_mysql(func_name, result)
#                     break
#
#             return result
#
#         return wrapper
#
#     return decorator
#
#
# # def save_log_to_mysql(func_name: str, args: tuple, kwargs: dict, result):
# def save_log_to_mysql(func_name: str, result):
#     # Connect to MySQL
#     conn = mysql.connector.connect(
#         host='your_host',
#         user='your_username',
#         password='your_password',
#         database='your_database'
#     )
#     cursor = conn.cursor()
#
#     # Prepare SQL query
#     sql = "INSERT INTO function_logs (function_name, arguments, keyword_arguments, result_type, result) " \
#           "VALUES (%s, %s, %s, %s, %s)"
#
#     # Convert arguments and keyword arguments to strings
#     args_str = ', '.join(map(str, args))
#     kwargs_str = ', '.join(f"{key}={value}" for key, value in kwargs.items())
#
#     # Determine result type and convert result to string if needed
#     result_type = type(result).__name__
#     # if isinstan