import logging
import random

from mTree.microeconomic_system.directive_decorators import *
from mTree.microeconomic_system.environment import Environment
from mTree.microeconomic_system.message import Message

import random

@directive_enabled_class
class VCMEnvironment(Environment):
    def __init__(self):
        pass

    def prepare(self):
        self.log_message(f'<E> prepare:')
        self.log_message(self.address_book)
        #same endowment for each agent
        self.endowment = self.get_property("endowment")
        # list of lists of buyer values, one list per buyer
        self.group_rate = self.get_property("group_rate") 
        # get num_participants
        self.num_participants = self.get_property("num_participants") 
        self.num_cooperators = self.get_property("num_cooperators")
        self.num_defectors = self.get_property("num_defectors")
        self.num_conditional_cooperators = self.get_property("num_conditional_cooperators")
        self.total_rounds = self.get_property("total_rounds")
        #self.num_agents = self.address_book.num_agents()
        self.round = 1
        msg_out = f"endowment: {self.endowment}, group_rate: {self.group_rate}, "
        msg_out += f"num_participants: {self.num_participants}, "
        msg_out += f"num_agents: {self.num_agents}, total_rounds: {self.total_rounds}"
        self.log_message(f'<E> prepare: {msg_out}')

    @directive_decorator("start_environment")
    def start_environment(self, message: Message):
        """
        Message handler for first message in simulation.
        """
        #self.set_reminder('end', 10)
        agent_types = self.make_agent_types()
        self.make_agent_data(agent_types)
        self.agents_reported = 0
        for agent_name, agent in self.agent_data.items():
            self.send_message('init_agent', agent_name, agent)
