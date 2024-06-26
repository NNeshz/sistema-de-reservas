import Home from "@/components/pages/Home";
import Reviews from "@/components/pages/Reviews";
import WholeBadge from "@/components/shared/WholeBadge";

const page = () => {
  return (
    <div className="w-full">
      <Home />
      <WholeBadge phrase="DELICIOUS FOOD, UNFORGETTABLE MOMENTS, JOIN US TODAY!" />
      <Reviews />
    </div>
  );
};

export default page;
