from collective.grok import gs
from reddplusid.project import MessageFactory as _

@gs.importstep(
    name=u'reddplusid.project', 
    title=_('reddplusid.project import handler'),
    description=_(''))
def setupVarious(context):
    if context.readDataFile('reddplusid.project.marker.txt') is None:
        return
    portal = context.getSite()

    # do anything here
