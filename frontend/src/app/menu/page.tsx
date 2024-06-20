import MaxWidthWrapper from "@/components/MaxWidthWrapper";
import { AspectRatio } from "@/components/ui/aspect-ratio";
import { categoriesData } from "@/json/fakeData";
import Image from "next/image";
import Link from "next/link";

const MenuPage = () => {  
  return (
    <div>
      <MaxWidthWrapper className="px-4 mb-14">
        <section className="mt-4 md:my-10">
          <p className="text-xl font-semibold md:text-2xl">¡Disfruta!</p>
          <h2 className="text-3xl font-bold md:text-6xl">
            Conoce nuestro menú de{" "}
            <p className="text-yellow-400">alimentos y bebidas.</p>
          </h2>
        </section>
        <section>
          {Object.entries(categoriesData).map(([category, items]) => (
            <div key={category} className="mt-4">
              <h3 className="text-xl font-semibold rounded-xl my-2 md:text-4xl md:mt-12">
                {category}
              </h3>
              <ul className="grid grid-cols-2 gap-8 md:grid-cols-3">
                {items.map((item) => (
                  <li key={item.name} className="rounded-md">
                    <Link
                      href={item.href}
                    >
                      <AspectRatio ratio={1 / 1}>
                        <Image
                          src={item.image}
                          alt="Dish 1"
                          fill
                          objectFit="cover"
                          quality={100}
                          className="rounded-lg"
                        />
                      </AspectRatio>
                    </Link>
                    <h4 className="text-center mt-2 font-semibold md:text-2xl ">
                      {item.name}
                    </h4>
                  </li>
                ))}
              </ul>
            </div>
          ))}
        </section>
      </MaxWidthWrapper>
    </div>
  );
};

export default MenuPage;
