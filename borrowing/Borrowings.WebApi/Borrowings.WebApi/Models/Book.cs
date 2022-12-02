using MongoDB.Bson;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Borrowings.WebApi.Models
{
    public class Book
    {
        public string _id { get; set; }
        public string Title { get; set; }
    }
}
