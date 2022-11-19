using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Borrowings.WebApi.Data
{
    public class BorrowingDbSettings
    {
        public string ConnectionString { get; set; } = null!;

        public string DatabaseName { get; set; } = null!;

        public string BorrowingsCollectionName { get; set; } = null!;
    }
}
