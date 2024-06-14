import HomePage from "@/components/pages/HomePage";
import TopDishesPage from "@/components/pages/TopDishesPage";
import WelcomePage from "@/components/pages/WelcomePage";

export default function Home() {
  return (
    <>
      {/* <BentoGrid>
          {landingPageData.map((item) => (
            <BentoCard {...item} key={item.name} />
          ))}
        </BentoGrid> */}
      <HomePage />
      <WelcomePage />
      <TopDishesPage />
    </>
  );
}
