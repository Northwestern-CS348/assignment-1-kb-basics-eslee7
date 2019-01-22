import read, copy
from util import *
from logical_classes import *


class KnowledgeBase(object):
    def __init__(self, facts=[], rules=[]):
        self.facts = facts
        self.rules = rules

    def __repr__(self):
        return 'KnowledgeBase({!r}, {!r})'.format(self.facts, self.rules)

    def __str__(self):
        string = "Knowledge Base: \n"
        string += "\n".join((str(fact) for fact in self.facts)) + "\n"
        string += "\n".join((str(rule) for rule in self.rules))
        return string

    def kb_assert(self, fact):
        """Assert a fact or rule into the KB

        Args:
            fact (Fact or Rule): Fact or Rule we're asserting in the format produced by read.py
        """
        print("Asserting {!r}".format(fact))
        if (isinstance(fact, Fact)):
            if (fact not in self.facts):
                self.facts.append(fact)
            else:
                print('kb_assert: Fact is already in database. ')
        else:
            print('kb_assert: Argument is not a fact')


        
    def kb_ask(self, fact):
        """Ask if a fact is in the KB

        Args:
            fact (Fact) - Fact to be asked

        Returns:
            ListOfBindings|False - ListOfBindings if result found, False otherwise
        """
        print("Asking {!r}".format(fact))
        if isinstance(fact, Fact):
            is_match = False
            bindings_list = ListOfBindings()
            for kb_fact in self.facts:
                potential_fact_bindings = match(fact.statement, kb_fact.statement)
                if potential_fact_bindings:
                    is_match = True
                    bindings_list.add_bindings(potential_fact_bindings)
            if is_match:
                return bindings_list
            return False
        else:
            print("kb_ask: Argument is not a fact")


