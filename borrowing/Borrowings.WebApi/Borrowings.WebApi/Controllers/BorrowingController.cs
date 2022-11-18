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

        [HttpPost]
        public async Task<IActionResult> Post(Borrowing item)
        {
            await _service.Create(item);

            return CreatedAtAction(nameof(Get), new { id = item.Id }, item);
        }

        [HttpPut("{id:length(24)}")]
        public async Task<IActionResult> Update(int id, Borrowing item)
        {
            var borrowing = await _service.Get(id);

            if (borrowing is null)
            {
                return NotFound();
            }

            item.Id = borrowing.Id;

            await _service.Update(id, item);

            return NoContent();
        }

        [HttpDelete("{id:length(24)}")]
        public async Task<IActionResult> Delete(int id)
        {
            var borrowing = await _service.Get(id);

            if (borrowing is null)
            {
                return NotFound();
            }

            await _service.Delete(id);

            return NoContent();
        }
    }
}
