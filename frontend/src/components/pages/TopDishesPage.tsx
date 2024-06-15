import MaxWidthWrapper from "../MaxWidthWrapper";
import { topDishesData } from "@/json/fakeData";
import TopDish from "../TopDish";
import Link from "next/link";

const TopDishesPage = () => {
  return (
    <div className="w-full h-auto md:h-screen  flex justify-center items-center my-10 md:my-0">
      <MaxWidthWrapper className=" h-full w-full flex flex-col items-center px-8">
        <h3 className="text-4xl font-bold">Platillos Pupulares</h3>
        <p className="text-lg text-center">
          Conoce los platillos más populares de nuestro menú.
        </p>
        <div className="w-full grid grid-cols-1 md:grid-cols-3 gap-6 mt-10">
          {topDishesData.map((dish) => (
            <TopDish {...dish} key={dish.name} />
          ))}
        </div>
        <p className="mt-10">
          ¿Quieres ver más platillos?{" "}
          <Link href="/menu" className="text-yellow-400">
            Visita nuestro menú
          </Link>
        </p>
      </MaxWidthWrapper>
    </div>
  );
};

export default TopDishesPage;
