
from pythondi import Provider, configure, inject
import abc

class Repo:
    """Interface class"""
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get(self):
        pass


class SQLRepo(Repo):
    """Impl class"""
    def __init__(self):
        pass

    def get(self):
        print('SQLRepo')

class Usecase:
    @inject()
    def __init__(self, repo: Repo):
        self.repo = repo

def home():
    usecase = Usecase()
    usecase.repo.get()
    print('Home')
    return ({'hello': 'world'})




if __name__ == '__main__':
    provider = Provider()
    provider.bind(Repo, SQLRepo)
    configure(provider=provider)
    home()
    
# OUTPUT 
# SQLRepo
# Home