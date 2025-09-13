import React, { useEffect } from "react";
import TruthLensHeader from "@/components/TruthLensHeader";
import HeroSection from "@/components/HeroSection";
import HowItWorksSection from "@/components/HowItWorksSection";
import TrendsSection from "@/components/TrendsSection";
import EducationSection from "@/components/EducationSection";
import FinalCTASection from "@/components/FinalCTASection";
import TruthLensFooter from "@/components/TruthLensFooter";

// Streamlit integration
declare global {
  interface Window {
    Streamlit: any;
  }
}

const Index = () => {
  useEffect(() => {
    // Initialize Streamlit communication
    if (window.Streamlit) {
      window.Streamlit.setComponentReady();
      window.Streamlit.setFrameHeight(1000);
    }
  }, []);

  return (
    <div id="truthlens-root" className="min-h-screen flex flex-col">
      <TruthLensHeader />
      <main className="flex-1">
        <HeroSection />
        <HowItWorksSection />
        <TrendsSection />
        <EducationSection />
        <FinalCTASection />
      </main>
      <TruthLensFooter />
    </div>
  );
};

export default Index;
