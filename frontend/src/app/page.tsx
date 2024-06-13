import MaxWidthWrapper from "@/components/MaxWidthWrapper";
import { BentoGrid, BentoCard } from "@/components/magicui/BentoGrid";
import { landingPageData } from "@/json/fakeData";

export default function Home() {
  return (
    <>
      <MaxWidthWrapper className="my-2">
        <BentoGrid>
          {landingPageData.map((item) => (
            <BentoCard {...item} key={item.name} />
          ))}
        </BentoGrid>
      </MaxWidthWrapper>
    </>
  );
}
