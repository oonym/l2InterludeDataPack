--
--  Table structure for fishing_skill_trees
--
CREATE TABLE IF NOT EXISTS `fishing_skill_trees` (
  `skill_id` int(10) NOT NULL default '0',
  `level` int(10) NOT NULL default '0',
  `name` varchar(25) NOT NULL default '',
  `sp` int(10) NOT NULL default '0',
  `min_level` int(10) NOT NULL default '0',
  `costid` int(10) NOT NULL default '0',
  `cost` int(10) NOT NULL default '0',
  `isfordwarf` int(1) NOT NULL default '0',
  PRIMARY KEY  (`skill_id`,`level`)
) TYPE=MyISAM;
--
--  Records for table fishing_skill_trees
--

