from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, DeclarativeBase, relationship, sessionmaker
from typing import List
from typing import Optional
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

# Создание базы данных SQLite в памяти
engine = create_engine('sqlite:///books_authors.db', echo=True)


class Base(DeclarativeBase):
    pass


# Ассоциативная таблица для отношения "многие ко многим" между книгами и авторами
books_authors = Table(
    'books_authors',
    Base.metadata,
    Column('author_id', Integer, ForeignKey('authors.id')),
    Column('book_id', Integer, ForeignKey('books.id'))
)

# Модель для авторов


class Author(Base):
    __tablename__ = 'authors'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), nullable=False)
    books: Mapped[List["Book"]] = relationship(
        # book_authors is a table name
        secondary=books_authors,
        back_populates='authors'
    )

    def __repr__(self):
        return f"<Author(name={self.name})>"

# Модель для книг


class Book(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30), nullable=False)
    authors: Mapped[List["Author"]] = relationship(
        secondary=books_authors,
        back_populates='books'
    )

    def __repr__(self):
        return f"<Book(title={self.title})>"


# Создание всех таблиц в базе данных
Base.metadata.create_all(engine)

# Создание сессии для взаимодействия с базой данных
with Session(engine) as session:
    # Добавление данных (авторов и книг)
    author1 = Author(name='J.K. Rowling')
    author2 = Author(name='George R.R. Martin')
    book1 = Book(title='Harry Potter and the Philosopher\'s Stone')
    book2 = Book(title='Harry Potter and the Chamber of Secrets')
    book3 = Book(title='A Game of Thrones')
    book4 = Book(title='A Clash of Kings')

    # Связь книг с авторами
    author1.books = [book1, book2]
    author2.books = [book3, book4]

    # Добавление объектов в сессию
    session.add_all([author1, author2])
    session.commit()

    # Вывод информации о книгах, написанных авторами
    authors = session.query(Author).all()
    for author in authors:
        print(f"{author.name} wrote the following books:")
        for book in author.books:
            print(f"- {book.title}")
