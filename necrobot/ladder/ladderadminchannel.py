from necrobot.botbase import cmd_seedgen
from necrobot.botbase.botchannel import BotChannel
from necrobot.ladder import cmd_ladder
from necrobot.league import cmd_league
from necrobot.league import cmd_leaguestats
from necrobot.user import cmd_user


class LadderAdminChannel(BotChannel):
    def __init__(self):
        BotChannel.__init__(self)
        self.channel_commands = [
            # cmd_ladder.Automatch(self),
            cmd_league.CloseFinished(self),
            # cmd_ladder.DropRacer(self),
            cmd_ladder.ForceRanked(self),

            cmd_seedgen.RandomSeed(self),

            cmd_leaguestats.LeagueFastest(self),
            cmd_leaguestats.LeagueStats(self),

            cmd_user.RTMP(self),
            cmd_user.UserInfo(self),
        ]
