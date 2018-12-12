import gym
#env = gym.make('CartPole-v0')
env = gym.make('FetchPickAndPlace-v1')
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        print('Action = %s ' % action, ' type= %s' % type(action))
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t+1))
            breakr
