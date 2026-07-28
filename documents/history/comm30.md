|  | 
| Measuring How NBA Players Help Their Teams WinBy Dan T. RosenbaumApril 30, 2004 Dan T. Rosenbaum is an economics professor at the University of North Carolina at Greensboro. Besides this statistical work, Rosenbaum has been cited in numerous publications for his expertise on issues related to the NBA collective bargaining agreement and especially the luxury tax. He is thankful to the many remarkable individuals who have helped him tremendously in better understanding the NBA. 
 I. Introduction “Good
players lead their teams to wins.”  “Lots of players can fill up a stat sheet,
but only the great ones are difference-makers.”  “The objective of a basketball game is not to
accumulate points or rebounds or assists, but
to win.  What statistic do you have
for that?”  When I talk with
knowledgeable basketball people who are skeptical of statistical analysis, I
hear variants on these statements over and over again.  The argument is that winning is important and
game statistics are only an imperfect measure of many of the contributions that
players make to winning. I
very much take this argument to heart. 
Basketball is not like baseball, a game structured around repeated
one-on-one contests between pitchers and batters, where the contributions to
winning of any given player can be measured well by individual game statistics.  Basketball is much more of a team game, and
as noted by Dean
Oliver, one of the leaders of statistical analysis is basketball, “teamwork is
the element of basketball most difficult to capture in any quantitative sense”
(p. 77).  While this argument often is overstated (as
much of this teamwork can be measured
using game statistics), the point still stands. 
These limitations have led to new approaches to measuring the value of basketball
players, approaches that make little use of game statistics like points,
rebounds, and assists. The most common approach is to compute plus/minus ratings that measure how point differentials change when a particular player is in the game versus when he is not. Hockey has used such a plus/minus system for years, and now 82games.com is the first to make these data available for the NBA. The logic of this approach is straightforward; teams should perform better when their good players are playing versus when they are not. The intuitive appeal of this approach has not escaped teams’ attention, and my understanding is that most teams use plus/minus ratings to some extent. However, these “unadjusted” plus/minus ratings do not measure the value of a player per se; they measure the value of the player relative to the players that substitute in for him. In addition, there are differences in the quality of players that players play with and against. A weak starter on a team with exceptionally good starters (relative to bench players) will generally get a very good unadjusted plus/minus rating – regardless of their actual contribution to the team. Thus,
a better measure of player value would “adjust” these plus/minus ratings to
account for the quality of players that a given player plays with and
against.  In addition, it would account
for home court advantage and for clutch time/garbage time play.  Thus, unlike in unadjusted plus/minus
ratings, these “adjusted” plus/minus ratings do not reward players simply for
being fortunate to being playing with teammates better than their
opponents.  Contributions for individual
players are isolated statistically. In this article, I develop adjusted
plus/minus ratings similar to the
WINVAL ratings designed by Jeff Sagarin and Wayne
Winston.[1]  I improve on past
efforts by combining estimates of player value using both pure adjusted
plus/minus ratings and a statistical index derived from these pure adjusted
plus/minus ratings. This hybrid approach leads to player ratings that unlike press accounts of WINVAL ratings, pass the “laugh test” (p. 181).  In addition, the results from this approach
are even less noisy than ratings based on traditional statistical indices
alone. Using
data from the 2002-03 and 2003-04 seasons (with the latter season being
weighted twice as heavily), I find that Kevin Garnett, Tracy McGrady, Andrei Kirilenko, Tim
Duncan, and Shaquille O’Neal are the five most
effective players in the NBA.  Replacing
an average player with one of these five players would result in a team
improving by about 14 points per 100 possessions or a little over 10 points per
game.  In other words, in 2003-04
replacing one of the average players on the Orlando Magic with one of these
five players likely would have made them a bit better than the New Jersey Nets
and Memphis Grizzlies. Perhaps
more importantly, with these adjusted plus/minus ratings I am able to estimate
what game statistics predict better performance on the court; these results
help explain why certain players have such high adjusted plus/minus ratings.  It appears that rebounds are less valuable
than typically assumed and steals, blocks, and avoiding turnovers are more
valuable.  It also appears that having
three point shooters on the floor helps teams and that players that can do it
all – score, rebound, and assist – are more valuable than simply the sum of
those game statistics.  In addition, even
after accounting for all of those game statistics, players who play more
minutes tend to be more valuable for their teams.  This finding suggests that coaches recognize
those contributions to the team that are not measured by game statistics, and
they play those players more minutes. In
this document I lay out a lot of the details of what I am doing and many of you
may want to skip over those details.  If
you just want to see my bottom-line ratings, go to Table 4 or
Table 5. II. A Discussion of the
Set-up and Results Here
is the set-up that I use. Every observation is a unit of time in a game where
no substitutions are made. There are more than 60,000 such observations
per year in 2002-03 and 2003-04. With these data I run the following
regression. X1
= 1 if player 1 is playing at home, = -1 if player 1 is
playing away, = 0 if player 1 is not
playing XK = 1 if player K is playing at home, =
-1 if player K is playing away, = 0 if player K
is not playing It is in this regression where the effects of the other players on
the floor are accounted for.  The bs in equation (1) measure
the point differential difference (measured per 100 possessions) of the given
player relative to the reference players, holding constant all of the players
that shared the floor with that player (and with the reference players), i.e.
holding the other players constant.  What
does this “holding other players constant” mean?  Strictly speaking, it means that we can take
a player and surround him with four teammates and five opponents and compare
how that player’s team would do versus how it would do if he was replaced by a
replacement player keeping all of the other players the same.  This is what is meant by “holding the other
players constant,” since we can repeat this exercise with any other combination
of other players.     Another
way to think of these bs is that they are
plus/minus statistics adjusted for the other players on the floor.  This takes out the effect of a player who is
fortunate to always play with Kevin Garnett or unfortunate enough to always
being matched with rookies or NBDL players. 
 Table
1 presents the results from equation (1) for the top twenty players among those
playing 250 minutes or more in the 2002-03 and 2003-04 seasons combined.  (I normalize these ratings so that the
average player is given a value of zero.) 
Kevin Garnett has by far and away the highest “pure” adjusted plus/minus
statistic, being a full 19.3 points per 100 possessions better than the average
player.  In addition, this estimate for
Garnett is quite precise with it being statistically significantly different from
most the rest of the players in the top ten. 
The rest of the top ten (with the exception of Nenę
and players with high standard errors and less than 1,000 minutes) are among
the top players in the game – Vince Carter, Andrei Kirilenko,
Dirk Nowitski, Tim Duncan, and Shaquille
O’Neal.  The next ten contains another
five players among the top players in the NBA – Rasheed
Wallace, Ray Allen, Tracy McGrady, Baron Davis, and
John Stockton. That
said, there are a number of outliers in the top
20.  Six of those nine outliers (Richie Frahm, Jason Hart, Mike
Sweetney, Mickael Pietrus, Earl Watson, and Carlos
Arroyo) have standard errors ranging from 4.3 to 6.3, so these players’ high
ratings could mostly reflect sampling variation – although Frahm’s
rating is so high that despite the high standard error and low number of
minutes, it probably is something more than sampling variation.  Three players (Nenę,
Jeff Foster, and Eric Williams) seem to have genuinely quite good ratings that
cannot be explained away by sampling variation. 
Foster replaced an All-Star in Brad Miller and his team did not miss a
beat, ending up with the best record in the League.  Nenę played major
minutes for a team that improved dramatically in 2003-04, and Eric Williams
played on two teams ( However,
even taking all of that into account, these ratings are quite noisy.  Another approach is probably necessary for
these rating to be that useful.  Below I
outline that approach which combines these pure adjusted plus/minus ratings
with ratings derived from the relationship between game statistics and these
pure adjusted plus/minus ratings. (I
also present offensive and defensive ratings that are based on the pure
adjusted plus/minus rating plus an “efficiency” rating that measures how many
points per possession are scored by both teams when a given player is one the
floor.  By combining these two measures,
I create offensive and defensive ratings. 
However, given that I am using two imprecisely estimated ratings to
arrive at these offensive ratings, I suspect these rating are measured with
quite a bit of error.) Table 1: Pure Adjusted
Plus/Minus Ratings for the Top 20 Players in 2002-03 and 2003-04 
 Notes: This table is limited
to the top 20 of the 420 players playing 250 minutes or more in 2002-03 and
2003-04 combined plus an aggregated observation for those playing less then 250
minutes. Observations from 2003-04 are weighted twice as heavily as those in
2002-03 and clutch time is given a higher weight and garbage time is given a
lesser (or zero) weight.  The Pure Adj. +/- Rating gives the
coefficient estimates from regression (1) above normalized so that the average
player is equal to zero and is measured in points per 100 possessions.  The SE
column gives the standard error for that rating.  Offensive
and Defensive Ratings are measured in points per 100 possessions and I also give
the Rank out of the 420 players.  Poss.
Used give the percentage of possessions used by a player with field goal
attempts, free throw attempts, assists, turnovers, and offensive rebounds with
the average being one fifth or 20%.  Offensive Efficiency gives the average
points scored per 100 possessions used, while Total Minutes gives the minutes played in 2002-03 and 2003-04.   One
approach to dealing with the imprecision of the pure adjusted plus/minus
ratings is to use game statistics (points, rebounds, assists, etc.) to measure
the correlation between these game statistics and the pure adjusted plus/minus
rating.  This indirectly measures how
these game statistics correlate with point differentials.  Equation (2) shows how this can be done in a
regression framework. (2)
       Y = b0 + b1X1 + b2X2 + . . . + b13X14 + e, where Y
is the pure adjusted plus minus statistic (the bs from the first
regression) X1 through X14 are game statistics described below in Table 2 Table
2 presents the Ordinary Least Squares (OLS) estimates and standard errors from
equation (2), along with sample means and standard deviations for each of the
variables.  The effects of most of the
game statistics are as expected with points, rebounds, assists, steals, and
blocks having a positive effect and field goal attempts, turnovers, and
personal fouls having a negative effect. Because
of the inclusion of the versatility variables multiplying points, rebounds,
assists, the marginal effect of another point (or rebound or assist) is not
simply given by its coefficient estimate. 
Evaluated at the mean level of points, rebounds, and assists, the
marginal effect of an additional point, assist, offensive rebound, and
defensive rebound is 1.08, 1.14, 0.78, and 0.11 points per 100 possessions,
respectively.  But because the
versatility coefficient is positive, these marginal effects are much higher for
players with lots of points, rebounds, and assists.  Also, note that once we account for the
versatility of players, offensive rebounders are more
valuable than defensive rebounders (although this
difference is not statistically significant). 
My earlier results showing offensive rebounders
being of less value probably was due to negative effect of having offensive
rebounding specialists on the floor who don’t score or assist much.  This negative effective is already accounted
for in the versatility measure. At
the mean level of effective field goal attempts, the marginal cost of another
two point field goal attempt is equal to 1.09 points per 100 possessions, but
at 25 effective field goal attempts per 40 minutes, the marginal cost is just
0.58 points per 100 possessions.  This
declining marginal cost likely reflects the value of players who can generate
field goal attempts as the shot clock is expiring or under extreme defensive
pressure.  Players who attempt lots of
three points and free throws appear to be more valuable than players who
specialize in two point field goal attempts. 
Steals and blocks both appear to be quite valuable, while turnovers are
very costly.  Personal fouls have a
small, but statistically insignificant, positive
effect, which could account for the possibility that better defenders tend to
guard players who generate more fouls. I
also include minutes played per game, and the results suggest that holding all
of these other game statistics constant, players who play more minutes tend to
help their team point differential.  This
result would be expected if coaches observe and reward contributions not picked
up in game statistics (e.g. good defense) by playing those players more
minutes.  Note, however, that the
coefficient is not huge.  Holding the
other game statistics constant, the difference between a 20
minutes per game player and a 40 minutes per game player is only 2.16 points per
100 possessions – about the same as an extra steal per 40 minutes. In
the future I hope to add height and age/experience to these regressions.  It appears to me that looking at the results
in many of the tables that young, inexperienced players tend to have lower pure
adjusted plus/minus ratings than their game statistics would suggest.  It seems that the young, inexperienced
players may not contribute as much to their teams in ways not picked up by game
statistics. Table 2: OLS Estimates
of the Effect of Game Statistics on Pure Adjusted Plus/Minus Ratings 
 Notes: This table is limited
to the top 20 of the 420 players playing 250 minutes or more in 2002-03 and
2003-04 combined plus an aggregated observation for those playing less then 250
minutes.  All of
the game statistics are measured per 40 minutes and are pace-adjusted in order
to account for teams who average more possessions per minute played.  The regression is weighted by minutes played
with the 2003-04 season counting twice as much as the 2002-03 season.  Effective field goal attempts are equal
to field goal attempts plus 0.44 times free throw attempts.  With
the coefficient estimates in Table 2, it is possible to estimate statistical
plus/minus ratings, which is what I do in Table 3.  These ratings are much cleaner than those in Table
1, which is evident in two ways.  First,
the standard errors are generally much smaller in Table 3.[4]  The second is that there are fewer odd
players in this list, which is a function of the smaller standard errors, along
with expectations that are derived from seeing similar games statistics-based
ratings in the past.  Note, however, that
six of the top 10 using statistical plus/minus ratings in Table 3 are in the
top 20 on the pure adjusted plus/minus ratings in Table 1.  And arguably, only Brian Cardinal and Shawn
Bradley are true outliers in these ratings. Table 3: Statistical
Plus/Minus Ratings for the Top 20 Players in 2002-03 and 2003-04 
 Notes: This table is limited
to the top 20 of the 420 players playing 250 minutes or more in 2002-03 and
2003-04 combined plus an aggregated observation for those playing less then 250
minutes.  The Statistical Rating is estimated using equation (2) and is measured
in points per 100 possessions.  The SE column gives the standard error for
that rating.  Poss. Used give the percentage of possessions used by a player with
field goal attempts, free throw attempts, assists, turnovers, and offensive
rebounds with the average being one fifth or 20%.  Offensive
Efficiency gives the average points scored per 100 possessions used, while Total Minutes gives the minutes played
in 2002-03 and 2003-04.   In
Table 4 I present “overall” plus/minus ratings that combine the pure adjusted
plus/minus ratings in Table 1 and statistical plus/minus ratings in Table
3.  The equation for doing so is the follwing. (3)        OVERALL = a * PURE + (1 – a) * STATS, where OVERALL
is the overall plus/minus rating PURE
is the pure adjusted plus/minus rating from Table 1 STATS
is the statistical plus/minus rating from Table 3 a is the share of the
overall rating due to the pure rating (it is chosen to minimize the standard
error of the overall rating with the restriction that it fall between 10% and
90%, note that this will result in the pure rating counting less when it is
especially noisy) These overall plus/minus ratings presented in
Table 4 containing very few outliers.  Brian
Cardinal is probably the only true outlier, but over the past two seasons he
has been remarkably efficient with the highest offensive efficiency (tied with Peja Stojakovic) among the top 20
players.  These results confirm that the
players recognized among the best in the NBA also are the most instrumental in
improving their teams’ point differentials.  The surprises in this list are that (1) Kevin
Garnett is head and shoulders above any other player, (2) Andrei Kirilenko is an elite player in the NBA, and (3) Vince
Carter and Rasheed Wallace are much more effective
players than is commonly assumed.  Table 4: Overall
Plus/Minus Ratings for the Top 20 Players in 2002-03 and 2003-04 
 Notes: This table is limited
to the top 20 of the 420 players playing 250 minutes or more in 2002-03 and
2003-04 combined plus an aggregated observation for those playing less then 250
minutes.  The Overall Rating combines the pure adjusted plus/minus ratings and
statistical plus/minus ratings as described in equation (3) and is measured in
points per 100 possessions.  The SE column gives the standard error for
that rating.  a
is the share of the Overall Rating
due to the pure adjusted plus/minus rating. 
The Pure Adj. +/- Rating gives
the coefficient estimates from regression (1) normalized so that the average
player is equal to zero and is measured in points per 100 possessions.  The SE
column gives the standard error for that rating.  The Statistical
Rating is estimated using equation (2) and is measured in points per 100
possessions.  The SE column gives the standard error for that rating.  Poss.
Used give the percentage of possessions used by a player with field goal
attempts, free throw attempts, assists, turnovers, and offensive rebounds with
the average being one fifth or 20%.  Offensive Efficiency gives the average
points scored per 100 possessions used, while Total Minutes gives the minutes played in 2002-03 and 2003-04.   Table
5 is a continuation of Table 4 showing how players in the top 20 of the overall
plus/minus ratings rate on various rating systems.  It lists the rankings for the pure adjusted
plus/minus ratings in Table 1, the statistical plus/minus ratings in Table 3,
and the per 40 minutes efficiency
index computed by NBA.com.  Comparing
these rankings shows once again how noisy the pure adjusted plus/minus
statistics are.  Table 5: Overall
Plus/Minus Ratings and Comparison of Ratings for the Top 20 Players in 2002-03
and 2003-04  
 Notes: This table is limited
to the top 20 of the 420 players playing 250 minutes or more in 2002-03 and
2003-04 combined plus an aggregated observation for those playing less then 250
minutes.  The Overall Rating combines the pure adjusted plus/minus ratings and
statistical plus/minus ratings as described in equation (3) and is measured in
points per 100 possessions.  The SE column gives the standard error for
that rating.  Rankings out of the 420 players
are given for the pure adjusted plus/minus ratings in Table 1 (Pure), the statistical plus/minus
ratings in Table 3 (Stats), and the
per 40 minutes efficiency
index computed by NBA.com (Index).  Poss.
Used give the percentage of possessions used by a player with field goal
attempts, free throw attempts, assists, turnovers, and offensive rebounds with
the average being one fifth or 20%.  Offensive Efficiency gives the average
points scored per 100 possessions used, while Total Minutes gives the minutes played in 2002-03 and 2003-04.   If you have any questions or comments about this analysis, feel free to call me or e-mail me. When possible, I will incorporate comments on this analysis. ** I thank . . . and other anonymous individuals for comments
on this analysis.  All errors or
mistakes, however, remain my own.  Also,
all conclusions are my own and do not reflect on anyone who might have aided me
in this analysis.  This analysis can be
used in whole or in part, as long as (1) this piece is credited to Dan Rosenbaum,
(2) a link to the latest version of this analysis (http://www.uncg.edu/eco/rosenbaum/NBA/winval2.htm)
is included, and (3) I have given express permission
for this use (e-mail
me). [1] Jeff Sagarin has successfully applied this methodology to teams for years and to individuals in non-team sports, such as golf and tennis, but this is the first time that I know of that this methodology has been applied to a individuals in a team sport. The Dallas Mavericks reportedly are paying more than $100,000 per year for this WINVAL system, which according to my knowledge is by far the greatest sum being paid to outside statistical consultants in the NBA. [2] In an observation where either the home or away team has zero possessions, the average home (or away) points per possession is used instead. If both teams have zero possessions, then the observation is deleted. [3] Here is my exact code. Clock measures the
minutes elapsed in the game
at the beginning of the observation. Three minutes left in the game (in regulation or in overtime) is
counted as 45. Margin is the absolute
value of the difference in scores at the beginning of the observation. [4] This standard error consists of two parts. The first is due to sampling variation from only observing players for a limited number of minutes. The second is due to the assumption that statistics ignore 15 percent of the true contributions of players, implying that even if an infinite number of games were observed, there would still be a standard error associated with the statistical plus/minus rating. 
 | |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
|  | |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
Copyright © 2004 by 82games.com, All Rights Reserved