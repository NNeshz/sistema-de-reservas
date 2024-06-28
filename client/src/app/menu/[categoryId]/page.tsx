// TODO: Create a function to fetch all the products of this category

import MaxWidthWrapper from "@/components/shared/MaxWidthWrapper";
import DishDetailedCard from "@/components/shared/DishDetailedCard";

const dishesOfCategoryAndDetails = {
  id: 11,
  name: "Subcategory Name",
  dishes: [
    {
      id: 1,
      name: "Dish Name",
      description: "Dish Description more than 10 words and something else",
      price: 10,
      img: "https://rb.gy/wjkwg7",
    },
    {
      id: 2,
      name: "Dish Name",
      description: "Dish Description more than 10 words and something else",
      price: 10,
      img: "https://rb.gy/wjkwg7",
    },
    {
      id: 3,
      name: "Dish Name",
      description: "Dish Description more than 10 words and something else",
      price: 10,
      img: "https://rb.gy/wjkwg7",
    },
    {
      id: 4,
      name: "Dish Name",
      description: "Dish Description more than 10 words and something else",
      price: 10,
      img: "https://rb.gy/wjkwg7",
    },
    {
      id: 5,
      name: "Dish Name",
      description: "Dish Description more than 10 words and something else",
      price: 10,
      img: "https://rb.gy/wjkwg7",
    },
    {
      id: 6,
      name: "Dish Name",
      description: "Dish Description more than 10 words and something else",
      price: 10,
      img: "https://rb.gy/wjkwg7",
    },
    {
      id: 7,
      name: "Dish Name",
      description: "Dish Description more than 10 words and something else",
      price: 10,
      img: "https://rb.gy/wjkwg7",
    },
    {
      id: 8,
      name: "Dish Name",
      description: "Dish Description more than 10 words and something else",
      price: 10,
      img: "https://rb.gy/wjkwg7",
    },
    {
      id: 9,
      name: "Dish Name",
      description: "Dish Description more than 10 words and something else",
      price: 10,
      img: "https://rb.gy/wjkwg7",
    },
    {
      id: 10,
      name: "Dish Name",
      description: "Dish Description more than 10 words and something else",
      price: 10,
      img: "https://rb.gy/wjkwg7",
    },
    {
      id: 11,
      name: "Dish Name",
      description: "Dish Description more than 10 words and something else",
      price: 10,
      img: "https://rb.gy/wjkwg7",
    },
    {
      id: 12,
      name: "Dish Name",
      description: "Dish Description more than 10 words and something else",
      price: 10,
      img: "https://rb.gy/wjkwg7",
    },
    {
      id: 13,
      name: "Dish Name",
      description: "Dish Description more than 10 words and something else",
      price: 10,
      img: "https://rb.gy/wjkwg7",
    },
    {
      id: 14,
      name: "Dish Name",
      description: "Dish Description more than 10 words and something else",
      price: 10,
      img: "https://rb.gy/wjkwg7",
    },
  ],
};

const page = () => {
  return (
    <div className="mt-4">
      <MaxWidthWrapper className="flex flex-col gap-y-4">
        <h2 className="text-3xl font-bold">This are {dishesOfCategoryAndDetails.name}</h2>
        <section className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {dishesOfCategoryAndDetails.dishes.map((dish, index) => (
            <DishDetailedCard key={index} {...dish} />
          ))}
        </section>
      </MaxWidthWrapper>
    </div>
  );
};

export default page;
