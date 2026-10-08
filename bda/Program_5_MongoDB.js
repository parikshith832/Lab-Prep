//Implement functions: Count-Sort-Limit-Skip- Aggregate using mango DB.
//OPEN mongosh 
use experimentFiva

db.createCollection("myCollection")

for (let i = 0; i < 10000; i++) {
    db.myCollection.insert({
        name: "Person" + i,
        age: Math.floor(Math.random() * 100),
        city: ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"][Math.floor(Math.random() * 5)]
    });
}

db.myCollection.find().count()
db.myCollection.find().skip(9999)
db.myCollection.find().limit(2)
db.myCollection.find().count()
db.myCollection.find({age: {$gt: 99}})
