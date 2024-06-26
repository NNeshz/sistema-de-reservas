import Categories from "@/components/pages/Categories";
import Home from "@/components/pages/Home";
import Reviews from "@/components/pages/Reviews";
import WholeBadge from "@/components/shared/WholeBadge";

const page = () => {
  return (
    <div className="w-full">
      <Home />
      <WholeBadge phrase="DELICIOUS FOOD, UNFORGETTABLE MOMENTS, JOIN US TODAY!" />
      <Reviews />
      <Categories />
    </div>
  );
};

export default page;
