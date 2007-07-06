# Contributed by Kilkenny to the Official L2J Datapack Project.
# with little cleanups by DrLecter.
# Visit http://www.l2jdp.com/trac if you find a bug.
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

qn = "51_OFullesSpecialBait"

#NPC
OFULLE = 31572
#ITEMS
LOST_BAIT = 7622
#REWARDS
ICY_AIR_LURE = 7611
#MOB
FETTERED_SOUL = 20552

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
   htmltext = event
   if event == "31572-03.htm" :
     st.set("cond","1")
     st.setState(STARTED)
     st.playSound("ItemSound.quest_accept")
   elif event == "31572-07.htm" and st.getQuestItemsCount(LOST_BAIT) == 100 :
     htmltext = "31572-06.htm"
     st.giveItems(ICY_AIR_LURE,4)
     st.takeItems(LOST_BAIT,-1)
     st.playSound("ItemSound.quest_finish")
     st.exitQuest(1)
   return htmltext

 def onTalk (Self,npc,player):
   htmltext = "<html><head><body>I have nothing to say you</body></html>"
   st = player.getQuestState(qn)
   if not st : return htmltext
   npcId = npc.getNpcId()
   id = st.getState()
   cond = st.getInt("cond")
   if id == COMPLETED :
      htmltext = "<html><head><body>This quest have already been completed.</body></html>"
   elif cond == 0 :
      if player.getLevel() >= 36 :
         htmltext = "31572-01.htm"
      else:
         htmltext = "31572-02.htm"
         st.exitQuest(1)
   elif id == STARTED :
      if st.getQuestItemsCount(LOST_BAIT) == 100 :
         htmltext = "31572-04.htm"
      else :
         htmltext = "31572-05.htm"
   return htmltext

 def onKill (self,npc,player):
   partyMember = self.getRandomPartyMember(player,"1")
   if not partyMember : return
   st = partyMember.getQuestState(qn)
   if st.getState() == STARTED :
      count = st.getQuestItemsCount(LOST_BAIT)
      if st.getInt("cond") == 1 and count < 100 :
         st.giveItems(LOST_BAIT,1)
      if count == 99 :
         st.playSound("ItemSound.quest_middle")
         st.set("cond","2")
      else :
         st.playSound("ItemSound.quest_itemget")
   return

QUEST       = Quest(51,qn,"O'Fulle's Special Bait")
CREATED     = State('Start', QUEST)
STARTED     = State('Started', QUEST)
COMPLETED   = State('Completed', QUEST)

QUEST.setInitialState(CREATED)
QUEST.addStartNpc(OFULLE)
QUEST.addTalkId(OFULLE)

QUEST.addKillId(FETTERED_SOUL)
STARTED.addQuestDrop(FETTERED_SOUL,LOST_BAIT,1)

print "importing quests: 51: O'Fulle's Special Bait"