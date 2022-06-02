# 学生信息管理框架

- 项目使用[poetry](https://python-poetry.org/)管理虚拟环境和依赖，因此需要在全局安装该工具。
- 项目使用[yapf](https://pypi.org/project/yapf/)保证代码风格一致，提交代码前需要运行格式化命令`poetry run isort . && poetry run yapf . --recursive -i `，具体见Makefile
开发使用的Python虚拟环境通过`poerty`管理，在`poetry`安装完成的情况下，使用以下命令初始化环境:

```shell
# 在pyproject.toml所在的同级目录执行
poetry install

**启动开发服务器**:
python manage.py runserver
此时应该可以访问文档服务器<http://127.0.0.1:8000/docs>
模拟登录token：doublekaitoken