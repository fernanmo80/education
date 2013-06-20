use blog;
db.posts.aggregate([
    /* now group by comments, counting each tag */
    {"$group": 
     {"_id":"$comments",
      "count":{$sum:1}
     }
    }
    ])
