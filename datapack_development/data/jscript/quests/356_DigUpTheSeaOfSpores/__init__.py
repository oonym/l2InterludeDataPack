# Made by disKret
import sys
from net.sf.l2j.gameserver.model.quest import State
from net.sf.l2j.gameserver.model.quest import QuestState
from net.sf.l2j.gameserver.model.quest.jython import QuestJython as JQuest

#NPC
GAUEN = 7717

#MOBS
SPORE_ZOMBIE = 562
ROTTING_TREE = 558

#QUEST ITEMS
CARNIVORE_SPORE = 5865
HERBIBOROUS_SPORE = 5866

class Quest (JQuest) :

 def __init__(self,id,name,descr): JQuest.__init__(self,id,name,descr)

 def onEvent (self,event,st) :
   htmltext = event
   if event == "7717-5.htm" :
     if st.getPlayer().getLevel() >= 43 :
       st.set("cond","1")
       st.setState(STARTED)
       st.playSound("ItemSound.quest_accept")
     else :
       htmltext = "7717-4.htm"
       st.exitQuest(1)
   elif event in [ "7717-10.htm", "7717-9.htm" ] :
     if event == "7717-9.htm" :
        st.giveItems(57,44000)
     else :
        st.addExpAndSp(36000,2600)
     st.takeItems(CARNIVORE_SPORE,50)
     st.takeItems(HERBIBOROUS_SPORE,50)
     st.playSound("ItemSound.quest_finish")
     st.exitQuest(1)
   return htmltext

 def onTalk (Self,npc,st):
   htmltext = "<html><head><body>I have nothing to say you</body></html>"
   id = st.getState()
   cond = st.getInt("cond")
   if cond == 0 :
     htmltext = "7717-0.htm"
   elif cond <> 3 :
     htmltext = "7717-6.htm"
   else :
     htmltext = "7717-7.htm"
   return htmltext

 def onKill (self,npc,st):
   npcId = npc.getNpcId()
   carn=st.getQuestItemsCount(CARNIVORE_SPORE)
   herb=st.getQuestItemsCount(HERBIBOROUS_SPORE)
   if npcId == SPORE_ZOMBIE :
     st.giveItems(CARNIVORE_SPORE,1)
     if carn == 49 :
       if herb == 50 :
         st.playSound("ItemSound.quest_middle")
         st.set("cond","3")
       else :
         st.playSound("ItemSound.quest_middle")
         st.set("cond","2")
     else :
       st.playSound("ItemSound.quest_itemget")	
   elif npcId == ROTTING_TREE :
     st.giveItems(HERBIBOROUS_SPORE,1)
     if herb == 49 :
       if carn == 50 :
         st.playSound("ItemSound.quest_middle")
         st.set("cond","3")
       else :
         st.playSound("ItemSound.quest_middle")
         st.set("cond","2")
     else:
       st.playSound("ItemSound.quest_itemget")	
   return

QUEST       = Quest(356,"356_DigUpTheSeaOfSpores","Dig Up The Sea Of Spores")
CREATED     = State('Start', QUEST)
STARTED     = State('Started', QUEST)

QUEST.setInitialState(CREATED)
QUEST.addStartNpc(GAUEN)

CREATED.addTalkId(GAUEN)
STARTED.addTalkId(GAUEN)

STARTED.addKillId(562)
STARTED.addKillId(558)

STARTED.addQuestDrop(GAUEN,CARNIVORE_SPORE,1)
STARTED.addQuestDrop(GAUEN,HERBIBOROUS_SPORE,1)

print "importing quests: 356: Dig Up The Sea Of Spores"