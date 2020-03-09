from aiohttp import web
import aiohttp_jinja2
import jinja2

from sgribt import fugtion

@aiohttp_jinja2.template('templete.html')
async def generetor(request):
    text = fugtion()
    return {'header': 'Space Dung', 
            'text': text}


app = web.Application()
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('.'))

app.add_routes([web.get('/', generetor)])


if __name__ == '__main__':
    web.run_app(app)

