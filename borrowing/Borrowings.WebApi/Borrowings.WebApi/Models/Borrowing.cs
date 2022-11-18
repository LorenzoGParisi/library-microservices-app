using MongoDB.Bson.Serialization.Attributes;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Borrowings.WebApi.Models
{
    public class Borrowing
    {
        [BsonId]
        [BsonRepresentation(MongoDB.Bson.BsonType.ObjectId)]
        public int Id { get; set; }
        [BsonElement("BorrowingItem")]
        public ICollection<Book> BorrowingItem { get; set; }
        [BsonElement("BorrowingStart")]
        [BsonRepresentation(MongoDB.Bson.BsonType.DateTime)]
        public DateTime BorrowingStart { get; set; }
        [BsonElement("BorrowingEnd")]
        [BsonRepresentation(MongoDB.Bson.BsonType.DateTime)]
        public DateTime BorrowingEnd { get; set; }
    }
}
}
