import AllCategories from "@/components/pages/AllCategories";
import MaxWidthWrapper from "@/components/shared/MaxWidthWrapper";
import type { Categories as CategoriesType } from "@/utils/types";

const categories: CategoriesType = {
  Drinks: [
    {
      id: 11,
      name: "Hot drinks",
      img: "https://rb.gy/wjkwg7",
    },
    {
      id: 12,
      name: "Cold drinks",
      img: "https://rb.gy/yqs191",
    },
    {
      id: 13,
      name: "Tea drinks",
      img: "https://rb.gy/svvnd0",
    },
    {
      id: 14,
      name: "Coffe",
      img: "https://rb.gy/4lvz9g",
    },
  ],
  Alimentos: [
    {
      id: 21,
      name: "Appetizers",
      img: "https://bit.ly/3RKH4WL",
    },
    {
      id: 22,
      name: "Main dishes",
      img: "https://bit.ly/4eFf5S8",
    },
    {
      id: 23,
      name: "Desserts",
      img: "https://bit.ly/3VJhcfa",
    },
    {
      id: 24,
      name: "Snacks",
      img: "https://bit.ly/4cjQ6Ce",
    },
  ],
  Batidos: [
    {
      id: 31,
      name: "Fruit smoothies",
      img: "https://bit.ly/4cnmGDl",
    },
    {
      id: 32,
      name: "Vegetable smoothies",
      img: "https://bit.ly/4cnmGDl",
    },
    {
      id: 33,
      name: "Protein smoothies",
      img: "https://bit.ly/4cnmGDl",
    },
  ],
  Carnes: [
    {
      id: 41,
      name: "Beef",
      img: "https://bit.ly/4eHj296",
    },
    {
      id: 42,
      name: "Chicken",
      img: "https://bit.ly/4eHj296",
    },
    {
      id: 43,
      name: "Pork",
      img: "https://bit.ly/4eHj296",
    },
    {
      id: 44,
      name: "Fish",
      img: "https://bit.ly/4eHj296",
    },
  ],
};

const page = () => {
  return (
    <div>
      <MaxWidthWrapper>
        <AllCategories categories={categories} />
      </MaxWidthWrapper>
    </div>
  );
};

export default page;
