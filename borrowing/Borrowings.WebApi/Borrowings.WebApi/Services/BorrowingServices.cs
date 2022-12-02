using Borrowings.WebApi.Data;
using Borrowings.WebApi.Models;
using Microsoft.Extensions.Options;
using MongoDB.Bson;
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
                connectionString: borrowingDbSettings.Value.ConnectionString);

            var mongoDatabase = mongoClient.GetDatabase(
                borrowingDbSettings.Value.DatabaseName);

            _context = mongoDatabase.GetCollection<Borrowing>(
                borrowingDbSettings.Value.CollectionName);
        }
        public async Task<List<Borrowing>> Get() =>
            await _context.Find(_ => true).ToListAsync();
        public async Task<Borrowing?> Get(string id) =>
            await _context.Find(x => x._id == id).FirstOrDefaultAsync();
        public async Task Create(Borrowing item) =>
            await _context.InsertOneAsync(item);
        public async Task Update(string id, Borrowing item) =>
            await _context.ReplaceOneAsync(x => x._id == id, item);
        public async Task Delete(string id) =>
            await _context.DeleteOneAsync(x => x._id == id);
    }
}
