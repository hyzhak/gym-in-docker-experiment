import gym

from PIL import Image

import gym
from gym import wrappers, logger


class RandomAgent:
    """The world's simplest agent!"""

    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        return self.action_space.sample()


def render_single_screenshot():
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


def run_agent(env_id):
    env = gym.make(env_id)

    # You provide the directory to write to (can be an existing
    # directory, including one with existing data -- all monitor files
    # will be namespaced). You can also dump to a tempdir if you'd
    # like: tempfile.mkdtemp().
    outdir = './tmp/random-agent-results'
    env = wrappers.Monitor(env, directory=outdir, force=True)
    env.seed(0)
    agent = RandomAgent(env.action_space)

    episode_count = 100
    reward = 0
    done = False

    for i in range(episode_count):
        ob = env.reset()
        while True:
            action = agent.act(ob, reward, done)
            ob, reward, done, _ = env.step(action)
            if done:
                break
                # Note there's no env.render() here. But the environment still can open window and
                # render if asked by env.monitor: it calls env.render('rgb_array') to record video.
                # Video is not recorded every episode, see capped_cubic_video_schedule for details.

    # Close the env and write monitor result info to disk
    env.close()


run_agent('CartPole-v0')
