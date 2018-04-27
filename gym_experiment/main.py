import gym

from PIL import Image

# env = gym.make('Breakout-v0')
env = gym.make('CartPole-v0')
env.reset()
screenshot = env.render(mode='rgb_array')
print(screenshot.shape)
print(type(screenshot))

#
# works for atari (but doesn't work for 'CartPole-v0')
#
# env.env.ale.saveScreenPNG(b'test_image.png')

img = Image.fromarray(screenshot.astype('uint8'), 'RGB')
img.save('test_image-2.png')
# imsave(b'test_image-2.png', img)

#
# Without close for 'CartPole-v0' we would get error:
#
# Exception ignored in: <bound method Viewer.__del__ of <gym.envs.classic_control.rendering.Viewer object at 0x7efcffdab630>>
# Traceback (most recent call last):
#   File "/usr/local/lib/python3.6/site-packages/gym/envs/classic_control/rendering.py", line 143, in __del__
#   File "/usr/local/lib/python3.6/site-packages/gym/envs/classic_control/rendering.py", line 62, in close
#   File "/usr/local/lib/python3.6/site-packages/pyglet/window/xlib/__init__.py", line 480, in close
#   File "/usr/local/lib/python3.6/site-packages/pyglet/gl/xlib.py", line 345, in destroy
#   File "/usr/local/lib/python3.6/site-packages/pyglet/gl/base.py", line 334, in destroy
#   File "/usr/local/lib/python3.6/site-packages/pyglet/gl/xlib.py", line 335, in detach
#   File "/usr/local/lib/python3.6/site-packages/pyglet/gl/lib.py", line 97, in errcheck
# ImportError: sys.meta_path is None, Python is likely shutting down
#
env.close()
