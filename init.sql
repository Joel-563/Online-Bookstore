-- Create books table
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    price DECIMAL(10,2)
);

-- Insert sample data
INSERT INTO books (title, author, price) VALUES
('Atomic Habits', 'James Clear', 499.00),
('Deep Work', 'Cal Newport', 599.00),
('The Pragmatic Programmer', 'Andrew Hunt', 699.00),
('Clean Code', 'Robert C. Martin', 799.00),
('Introduction to Algorithms', 'Thomas H. Cormen', 999.00);
