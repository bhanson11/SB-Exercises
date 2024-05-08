-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Teams" (
    "team_id" int PRIMARY KEY,
    "team_name" text   NOT NULL,
    CONSTRAINT "pk_Teams" PRIMARY KEY (
        "team_id"
     ),
    "Wins" INT GENERATED ALWAYS AS (
        SELECT COUNT(*) FROM "Matches"
        WHERE "team1_id" = "Teams"."team_id" AND 
        "team1_score" > "team2_score"
        OR "team2_id" = "Teams"."team_id" AND 
        "team2_score" > "team1_score"
    ) STORED,
    "Draws" INT GENERATED ALWAYS AS (
        SELECT COUNT(*) FROM "Matches" 
        WHERE "team1_id" = "Teams"."team_id" AND 
        "team1_score" = "team2_score"
           OR "team2_id" = "Teams"."team_id" AND "team2_score" = "team1_score"
    ) STORED,
    "Losses" INT GENERATED ALWAYS AS (
        SELECT COUNT(*) FROM "Matches"
        WHERE "team1_id" = "Teams"."team_id" AND "team1_score" < "team2_score"
           OR "team2_id" = "Teams"."team_id" AND "team2_score" < "team1_score"
    ) STORED,
    "Points" INT GENERATED ALWAYS AS ("Wins" * 3 + "Draws") STORED
);

CREATE TABLE "Players" (
    "player_id" int   NOT NULL,
    "first_name" text   NOT NULL,
    "last_name" text   NOT NULL,
    "team_id" int   NOT NULL,
    CONSTRAINT "pk_Players" PRIMARY KEY (
        "player_id"
     )
);

CREATE TABLE "Matches" (
    "match_id" int   NOT NULL,
    "team1_id" int   NOT NULL,
    "team2_id" int   NOT NULL,
    "match_date" date   NOT NULL,
    "referee1_id" int   NOT NULL,
    "referee2_id" int   NOT NULL,
    "referee3_id" int   NOT NULL,
    "season_id" int   NOT NULL,
    CONSTRAINT "pk_Matches" PRIMARY KEY (
        "match_id"
     )
);

CREATE TABLE "Goals" (
    "goal_id" int   NOT NULL,
    "player_id" int   NOT NULL,
    "match_id" int   NOT NULL,
    "goal_time" time   NOT NULL,
    CONSTRAINT "pk_Goals" PRIMARY KEY (
        "goal_id"
     )
);

CREATE TABLE "Referees" (
    "referee_id" int   NOT NULL,
    "first_name" text   NOT NULL,
    "last_name" text   NOT NULL,
    CONSTRAINT "pk_Referees" PRIMARY KEY (
        "referee_id"
     )
);

CREATE TABLE "Seasons" (
    "season_id" int   NOT NULL,
    "start_date" date   NOT NULL,
    "end_date" date   NOT NULL,
    CONSTRAINT "pk_Seasons" PRIMARY KEY (
        "season_id"
     )
);

ALTER TABLE "Players" ADD CONSTRAINT "fk_Players_team_id" FOREIGN KEY("team_id")
REFERENCES "Teams" ("team_id");

ALTER TABLE "Matches" ADD CONSTRAINT "fk_Matches_team1_id" FOREIGN KEY("team1_id")
REFERENCES "Teams" ("team_id");

ALTER TABLE "Matches" ADD CONSTRAINT "fk_Matches_team2_id" FOREIGN KEY("team2_id")
REFERENCES "Teams" ("team_id");

ALTER TABLE "Matches" ADD CONSTRAINT "fk_Matches_referee1_id" FOREIGN KEY("referee1_id")
REFERENCES "Referees" ("referee_id");

ALTER TABLE "Matches" ADD CONSTRAINT "fk_Matches_referee2_id" FOREIGN KEY("referee2_id")
REFERENCES "Referees" ("referee_id");

ALTER TABLE "Matches" ADD CONSTRAINT "fk_Matches_referee3_id" FOREIGN KEY("referee3_id")
REFERENCES "Referees" ("referee_id");

ALTER TABLE "Matches" ADD CONSTRAINT "fk_Matches_season_id" FOREIGN KEY("season_id")
REFERENCES "Seasons" ("season_id");

ALTER TABLE "Goals" ADD CONSTRAINT "fk_Goals_player_id" FOREIGN KEY("player_id")
REFERENCES "Players" ("player_id");

ALTER TABLE "Goals" ADD CONSTRAINT "fk_Goals_match_id" FOREIGN KEY("match_id")
REFERENCES "Matches" ("match_id");

CREATE VIEW "TeamStandings" AS
SELECT
"team_id", "team_name", "Wins", "Draws", "Losses", "Points"
FROM "Teams";