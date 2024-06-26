import type { Categories as CategoriesType } from "@/utils/types";
import CategoryCard from "../shared/CategoryCard";

interface AllCategoriesProps {
  categories: CategoriesType;
}

const AllCategories = ({ categories }: AllCategoriesProps) => {
  return (
    <div className="w-full">
      {Object.entries(categories).map(([category, dishes]) => (
        <div key={category} className="mt-8">
          <h3 className="text-xl font-bold md:text-2xl">{category}</h3>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-4">
            {dishes.map(
              ({
                id,
                name,
                img,
              }: {
                id: number;
                name: string;
                img: string;
              }) => (
                <CategoryCard id={id} key={id} name={name} image={img} />
              )
            )}
          </div>
        </div>
      ))}
    </div>
  );
};

export default AllCategories;
