"""
High-level module for the standard Condorbot (Event Server) config.


Package Requirements
--------------------
gsheet
league
    match
        user
        botbase
        util
stats
stream


Dependencies
------------
cmd_condor
    botbase/
        necroevent
        commandtype
    util/
        server
condoradminchannel
    botbase/
        cmd_seedgen
        botchannel
    gsheet/
        cmd_sheet
    league/
        cmd_league
    user/
        cmd_user
condormainchannel
    botbase/
        cmd_admin
    league/
        cmd_league
    match/
        cmd_match
    stats/
        cmd_stats
    user/
        cmd_user
condormgr
    botbase/
        necroevent
        manager
    condor/
        cmd_condor
    gsheet/
        cmd_sheet
        sheetlib
        matchupsheet
        standingssheet
    league/
        leaguemgr
    match/
        matchutil
        match
        matchroom
    stats/
        statfn
    stream/
        vodrecord
    util/
        server
        singleton
        strutil
        rtmputil
condorpmchannel
    botbase/
        cmd_admin
        botchannel
    match/
        cmd_match
    stats/
        cmd_stats
    user/
        cmd_user
"""