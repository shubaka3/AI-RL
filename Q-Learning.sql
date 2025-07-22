CREATE TABLE [dbo].[User] (
    UserID INT IDENTITY(1,1) PRIMARY KEY,
    UserName NVARCHAR(255) NOT NULL,
    Email NVARCHAR(255) UNIQUE,
    CreatedAt DATETIME DEFAULT GETDATE()
);

CREATE TABLE [dbo].[Product] (
    ProductID INT IDENTITY(1,1) PRIMARY KEY,
    ProductName NVARCHAR(255) NOT NULL,
    Category NVARCHAR(255) NOT NULL,
    Price DECIMAL(10,2) NOT NULL CHECK (Price >= 0),
    CreatedAt DATETIME DEFAULT GETDATE()
);

CREATE TABLE [dbo].[UserDetail] (
    DetailID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT NOT NULL,
    ProductID INT NOT NULL,
    Action NVARCHAR(50) NOT NULL,  -- 'view', 'click', 'add_to_cart', 'purchase', 'rate'
    Rating INT NULL CHECK (Rating >= 1 AND Rating <= 5),
    Timestamp DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (UserID) REFERENCES [dbo].[User](UserID),
    FOREIGN KEY (ProductID) REFERENCES [dbo].[Product](ProductID)
);


-- Thêm 10 user mẫu
INSERT INTO [dbo].[User] (UserName, Email)
VALUES 
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com'),
('Charlie', 'charlie@example.com'),
('David', 'david@example.com'),
('Emma', 'emma@example.com'),
('Frank', 'frank@example.com'),
('Grace', 'grace@example.com'),
('Hannah', 'hannah@example.com'),
('Ivy', 'ivy@example.com'),
('Jack', 'jack@example.com');


-- Thêm 10 product mẫu
INSERT INTO [dbo].[Product] (ProductName, Category, Price)
VALUES 
('Laptop A', 'Electronics', 1200.00),
('Smartphone B', 'Electronics', 800.00),
('Headphones C', 'Electronics', 150.00),
('Sneakers D', 'Fashion', 90.00),
('T-shirt E', 'Fashion', 25.00),
('Coffee Mug F', 'Home', 10.00),
('Blender G', 'Home', 75.00),
('Novel H', 'Books', 20.00),
('Notebook I', 'Books', 5.00),
('Desk Lamp J', 'Home', 30.00);


-- Insert UserDetail ngẫu nhiên cho user 1 -> 10, product 1 -> 10
DECLARE @i INT = 1;

WHILE @i <= 1000
BEGIN
    INSERT INTO [dbo].[UserDetail] (UserID, ProductID, Action, Rating)
    VALUES (
        ABS(CHECKSUM(NEWID())) % 10 + 1,           -- Random UserID 1..10
        ABS(CHECKSUM(NEWID())) % 10 + 1,           -- Random ProductID 1..10
        CASE ABS(CHECKSUM(NEWID())) % 4 
            WHEN 0 THEN 'view'
            WHEN 1 THEN 'click'
            WHEN 2 THEN 'add_to_cart'
            ELSE 'purchase'
        END,
        CASE ABS(CHECKSUM(NEWID())) % 2 
            WHEN 0 THEN NULL
            ELSE ABS(CHECKSUM(NEWID())) % 5 + 1
        END
    )
    SET @i = @i + 1
END


CREATE TABLE [dbo].[UserRecommendation] (
    ID INT IDENTITY(1,1) PRIMARY KEY,
    UserID INT NOT NULL,
    ProductID INT NOT NULL,
    Score FLOAT NOT NULL,
    CreatedAt DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (UserID) REFERENCES [dbo].[User](UserID),
    FOREIGN KEY (ProductID) REFERENCES [dbo].[Product](ProductID)
);
