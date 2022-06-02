from rllab.rllab.core.serializable import Serializable
from rllab.rllab.envs.mujoco.ant_env import AntEnv
from sandbox.cpo.envs.mujoco_safe.mujoco_env_safe import SafeMujocoEnv
import numpy as np

class SafeAntEnv(SafeMujocoEnv, Serializable):

    MODEL_CLASS = AntEnv

