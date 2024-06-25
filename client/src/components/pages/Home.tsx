import DishCard from "../shared/DishCard";
import MaxWidthWrapper from "../shared/MaxWidthWrapper";
import { Separator } from "../ui/separator";

const popularDishes = [
  {
    name: "Pizza",
    description: "Delicious pizza with pepperoni and cheese. Add your ingredients as you like.",
    image: "https://rb.gy/uxr949",
  },
  {
    name: "BBQ Burger",
    description: "Juicy burger with BBQ sauce and bacon. With fries and a drink.",
    image: "https://rb.gy/60slyh",
  },
  {
    name: "Pasta",
    description: "Spaghetti with meatballs and tomato sauce.",
    image: "https://rb.gy/ly2qsf",
  },
  {
    name: "Sushi",
    description: "Sushi rolls with salmon and avocado. The sea in your plate.",
    image: "https://rb.gy/2w809o",
  },
];

const Home = () => {
  return (
    <section>
      <MaxWidthWrapper className="my-5">
        <h2 className="text-3xl font-bold">Popular dishes.</h2>
        <p className="text-sm text-zinc-600 mt-2">
          Taste the real flavor in your city, just by some clicks.
        </p>
        <Separator className="my-4" />
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-4">
          {popularDishes.map((dish) => (
            <DishCard
              key={dish.name}
              name={dish.name}
              description={dish.description}
              image={dish.image}
            />
          ))}
        </div>
      </MaxWidthWrapper>
    </section>
  );
};

export default Home;
