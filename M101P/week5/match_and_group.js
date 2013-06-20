
db.zips.aggregate([
                    {  $match: {
                        "pop":  { $gt:25000 }
                      }
                    }
                 ])



db.zips.aggregate([
    {$project: {
 	     first_char: {$substr : ["$city",0,1]},
     },
     {$match: { first_char : { $in: ['0','1','2','3','4','5']}  }}
   }
])

db.posts.aggregate(
     {$unwind: "$comments" },
	   {$group:{
			_id:"$comments.author",
			sumCommentsByAuthors:{$sum:1},
			countCommentsByAuthors:{$sum:"$comments"}            
    }
}
)


db.grades.aggregate( [ 
  { $unwind: "$scores"},
  { $match : { "scores.type" : { $in: [ 'exam', 'homework' ] } }},
  { $group : { _id: "class_id", "student_average" : { "$avg":"$score" }}}
]
