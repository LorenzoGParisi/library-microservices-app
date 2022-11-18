using Borrowings.WebApi.Models;
using Borrowings.WebApi.Services;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace Borrowings.WebApi.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class BorrowingController : ControllerBase
    {
        private readonly BorrowingServices _service;
        public BorrowingController(BorrowingServices borrowingServices) =>
            _service = borrowingServices;

        [HttpGet]
        public async Task<List<Borrowing>> Get() =>
            await _service.Get();

        [HttpGet("{id:length(24)}")]
        public async Task<ActionResult<Borrowing>> Get(int id)
        {
            var borrowing = await _service.Get(id);

            if (borrowing is null)
            {
                return NotFound();
            }

            return borrowing;
        }
    }
}
