using Microsoft.EntityFrameworkCore;
namespace Backend.Data

{
    public class UserDbContext : DbContext

    {
        public UserDbContext(DbContextOptions<UserDbContext> options) : base(options)
        {
        }
        public DbSet<Backend.Models.User> Users { get; set; }
        public DbSet<Backend.Models.Faculty> Faculties { get; set; }
        public DbSet<Backend.Models.Subject> Subjects { get; set; }
        public DbSet<Backend.Models.Enrollment> Enrollments { get; set; }
    }
}
