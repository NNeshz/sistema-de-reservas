import Image from "next/image";
import MaxWidthWrapper from "../MaxWidthWrapper";
import { Button, buttonVariants } from "../ui/button";
import Link from "next/link";
import { ArrowRight, CheckSquare, Table } from "lucide-react";
import { cn } from "@/lib/utils";

const HomePage = () => {
  return (
    <div className="relative h-[70vh] md:h-[85vh] w-full flex flex-col justify-center items-center text-white">
      <Image
        src="https://images.unsplash.com/photo-1540189549336-e6e99c3679fe"
        layout="fill"
        objectFit="cover"
        quality={80}
        alt="Plato de comida"
      />
      <div className="absolute inset-0 bg-gradient-to-t from-black to-transparent"></div>
      <div className="relative z-10 w-full">
        <MaxWidthWrapper className="px-4">
          <p className="md:text-xl md:pl-1">Experimenta el verdadero sabor.</p>
          <h2 className="text-4xl md:text-7xl">
            Experimenta los mejores <strong>platillos de la ciudad.</strong>
          </h2>
          <div className="mt-4 flex flex-col w-40 items-start gap-y-2">
            <Link
              href="/menu"
              className={cn(
                "gap-x-2 items-center",
                buttonVariants({
                  variant: "default",
                })
              )}
            >
              Ver menú <ArrowRight />{" "}
            </Link>
            <Link
              href="/menu"
              className={cn(
                "gap-x-2 items-center text-black",
                buttonVariants({
                  variant: "outline",
                })
              )}
            >
              Reservar <CheckSquare />{" "}
            </Link>
          </div>
        </MaxWidthWrapper>
      </div>
    </div>
  );
};

export default HomePage;
