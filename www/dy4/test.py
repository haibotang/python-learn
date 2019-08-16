import www.web.orm
from www.models import User
import asyncio

async def test(loop):
  await www.web.orm.create_pool(loop, user='root', password='root', db ='test')
  u = User(name='Test',email ='test@example.com',passwd='123456',image='about.blank')
  await u.save()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    print('Test finished.')
    loop.close()