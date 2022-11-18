using Borrowings.WebApi.Data;
using Borrowings.WebApi.Models;
using Microsoft.Extensions.Options;
using MongoDB.Driver;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Borrowings.WebApi.Services
{
    public class BorrowingServices
    {
        private readonly IMongoCollection<Borrowing> _context;

        public BorrowingServices(
            IOptions<BorrowingDbSettings> borrowingDbSettings)
        {
            var mongoClient = new MongoClient(
                borrowingDbSettings.Value.ConnectionString);

            var mongoDatabase = mongoClient.GetDatabase(
                borrowingDbSettings.Value.DatabaseName);

            _context = mongoDatabase.GetCollection<Borrowing>(
                borrowingDbSettings.Value.BooksCollectionName);
        }
    }
}
