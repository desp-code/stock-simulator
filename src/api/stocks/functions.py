from src.dao.stock_dao import StockDAO
from datetime import datetime

def get_stocks():
    """Returns a list of all stocks from the stock table"""
    stock_dao = StockDAO()
    result = stock_dao.get_stocks()
    return process_response(result)

def get_stock_by_symbol(symbol):
    """Returns all stocks specified by the provided stock symbol."""
    response = {}
    successful_response = {}
    error_response = {}
    stock_dao = StockDAO()
    result = stock_dao.get_stock_by_symbol(symbol)
    if len(result.all()) != 0:
        return process_response(result)
    else:
        error_response['message'] = "The requested resource was not found."
        error_response['code'] = '404'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response

def get_stock_by_id(id):
    """Returns all stocks specified by the provided stock id."""
    response = {}
    successful_response = {}
    error_response = {}
    stock_dao = StockDAO()
    result = stock_dao.get_stock_by_id(id)
    if len(result.all()) != 0:
        return process_response(result)
    else:
        error_response['message'] = "The requested resource was not found."
        error_response['code'] = '404'
        response['error'] = error_response
        response['timestamp'] = datetime.utcnow()
        return response

def process_response(query):
    """Takes a query and formats the attributes in the query. Returns the formatted attributes."""
    response = {}
    stocks = []
    for row in query:
        stock = {}
        stock['stock_id'] = row.stock_id
        stock['symbol'] = row.symbol
        stocks.append(stock)
    response['data'] = stocks
    response['timestamp'] = datetime.utcnow()
    return response
