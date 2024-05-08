-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Regions" (
    "region_id" int   NOT NULL,
    "region_name" string   NOT NULL,
    CONSTRAINT "pk_Regions" PRIMARY KEY (
        "region_id"
     ),
    CONSTRAINT "uc_Regions_region_name" UNIQUE (
        "region_name"
    )
);

CREATE TABLE "Users" (
    "user_id" int   NOT NULL,
    "username" string   NOT NULL,
    "preferred_region_id" int   NOT NULL,
    CONSTRAINT "pk_Users" PRIMARY KEY (
        "user_id"
     ),
    CONSTRAINT "uc_Users_username" UNIQUE (
        "username"
    )
);

CREATE TABLE "Posts" (
    "post_id" int   NOT NULL,
    "title" string   NOT NULL,
    "text" VARCHAR(200)   NOT NULL,
    "user_id" int   NOT NULL,
    "location" text   NOT NULL,
    "region_id" int   NOT NULL,
    CONSTRAINT "pk_Posts" PRIMARY KEY (
        "post_id"
     )
);

CREATE TABLE "Categories" (
    "category_id" int   NOT NULL,
    "category_name" string   NOT NULL,
    CONSTRAINT "pk_Categories" PRIMARY KEY (
        "category_id"
     ),
    CONSTRAINT "uc_Categories_category_name" UNIQUE (
        "category_name"
    )
);

CREATE TABLE "PostCategories" (
    "post_id" int   NOT NULL,
    "category_id" int   NOT NULL
);

ALTER TABLE "Regions" ADD CONSTRAINT "fk_Regions_region_id" FOREIGN KEY("region_id")
REFERENCES "Posts" ("region_id");

ALTER TABLE "Users" ADD CONSTRAINT "fk_Users_preferred_region_id" FOREIGN KEY("preferred_region_id")
REFERENCES "Regions" ("region_id");

ALTER TABLE "Posts" ADD CONSTRAINT "fk_Posts_user_id" FOREIGN KEY("user_id")
REFERENCES "Users" ("user_id");

ALTER TABLE "PostCategories" ADD CONSTRAINT "fk_PostCategories_post_id" FOREIGN KEY("post_id")
REFERENCES "Posts" ("post_id");

ALTER TABLE "PostCategories" ADD CONSTRAINT "fk_PostCategories_category_id" FOREIGN KEY("category_id")
REFERENCES "Categories" ("category_id");

