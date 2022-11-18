﻿using Borrowings.WebApi.Data;
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
        public async Task<List<Borrowing>> Get() =>
            await _context.Find(_ => true).ToListAsync();
        public async Task<Borrowing?> Get(int id) =>
            await _context.Find(x => x.Id == id).FirstOrDefaultAsync();
    }
}
