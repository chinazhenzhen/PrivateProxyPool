"""
web api
"""
from flask import Flask, g, jsonify

from proxypool.db import RedisClient

__all__ = ['app']

app = Flask(__name__)


def get_conn():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/random')
def get_proxy():
    """
    Get a proxy
    :return: 随机代理
    """
    conn = get_conn()
    return jsonify(conn.random())


@app.route('/all')
def get_all():
    """
    Get the proxy all.
    取出redis中的所用代理,json
    """
    conn = get_conn()
    return jsonify(conn.all())


@app.route('/count')
def get_counts():
    """
    Get the count of proxies
    :return: 代理池总量
    """
    conn = get_conn()
    return jsonify(conn.count())


if __name__ == '__main__':
    app.run()