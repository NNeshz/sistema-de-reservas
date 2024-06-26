import MaxWidthWrapper from "../shared/MaxWidthWrapper";
import CategoryCard from "../shared/CategoryCard";

const categories = {
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
};

const Categories = () => {
  return (
    <div>
      <MaxWidthWrapper className="my-5">
        <h2 className="text-3xl font-bold">Categories</h2>
        <p className="text-sm text-zinc-600 mt-2">
            Don&apos;t miss our delicious dishes. Choose your favorite category.
        </p>
        <div className="w-full">
          {Object.entries(categories).map(([category, dishes]) => (
            <div key={category} className="mt-8">
              <h3 className="text-xl font-bold md:text-2xl">{category}</h3>
              <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-4">
                {dishes.map(({ id, name, img}) => (
                  <CategoryCard
                    id={id}
                    key={id}
                    name={name}
                    image={img}
                  />
                ))}
              </div>
            </div>
          ))}
        </div>
      </MaxWidthWrapper>
    </div>
  );
};

export default Categories;
