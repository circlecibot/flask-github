from ..messages import Tree
from ..requests import TreeResponse
from ..requests import TreeListResponse

class GitDataTrees:
  def __init__(self, client):
    self.client = client

  def get_tree(self, repo, sha, recursive=False, user=None):
    url = 'repos/%s/%s/git/trees/%s' % (self.client.user(user), repo, sha)
    query = None
    if recursive:
      query = {'recursive': '1'}
    return self.client.get(url, query=query, msg_type=TreeListResponse)

  def create_tree(self, repo, tree, base_tree=None, user=None):
    msg = Tree(
      base_tree=base_tree,
      tree=tree)
    return self.client.post(
      'repos/%s/%s/git/trees' % (
        self.client.user(user), repo), msg, msg_type=TreeResponse)
