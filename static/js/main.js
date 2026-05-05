/**
 * GeoGamesMedieval — Основной JavaScript
 * Функционал: навигация, анимации, копирование и т.д.
 */

// ========================================
// Инициализация при загрузке DOM
// ========================================
document.addEventListener('DOMContentLoaded', function() {
    initNavbar();
    initScrollReveal();
    initScrollTop();
    initSmoothScroll();
});

// ========================================
// Навигация
// ========================================
function initNavbar() {
    const navbar = document.getElementById('navbar');
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.querySelector('.nav-menu');

    // Эффект при скролле
    window.addEventListener('scroll', function() {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Мобильное меню
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            const icon = navToggle.querySelector('i');
            if (navMenu.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });

        // Закрыть меню при клике на ссылку
        navMenu.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                navMenu.classList.remove('active');
                navToggle.querySelector('i').classList.remove('fa-times');
                navToggle.querySelector('i').classList.add('fa-bars');
            });
        });
    }
}

// ========================================
// Анимации при скролле (Scroll Reveal)
// ========================================
function initScrollReveal() {
    const elements = document.querySelectorAll('.scroll-reveal');

    if (!elements.length) return;

    // Функция проверки видимости элемента
    const checkVisibility = () => {
        elements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const elementBottom = element.getBoundingClientRect().bottom;
            const isVisible = elementTop < window.innerHeight * 0.9 && elementBottom > 0;

            if (isVisible) {
                element.classList.add('visible');
            }
        });
    };

    // Проверка при загрузке и при скролле
    checkVisibility();
    window.addEventListener('scroll', checkVisibility);
    window.addEventListener('resize', checkVisibility);
}

// ========================================
// Кнопка "Наверх"
// ========================================
function initScrollTop() {
    const scrollTopBtn = document.getElementById('scrollTop');

    if (!scrollTopBtn) return;

    const toggleScrollTop = () => {
        if (window.scrollY > 400) {
            scrollTopBtn.classList.add('visible');
        } else {
            scrollTopBtn.classList.remove('visible');
        }
    };

    scrollTopBtn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    window.addEventListener('scroll', toggleScrollTop);
    toggleScrollTop(); // Проверка при загрузке
}

// ========================================
// Плавная прокрутка для якорных ссылок
// ========================================
function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');

            // Пропускаем если это не якорь на странице
            if (href === '#' || href.length === 1) return;

            const target = document.querySelector(href);

            if (target) {
                e.preventDefault();

                // Учитываем высоту фиксированной навигации
                const headerOffset = 80;
                const elementPosition = target.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
}

// ========================================
// Утилиты
// ========================================

/**
 * Копирование текста в буфер обмена
 * @param {string} text - Текст для копирования
 * @returns {Promise<boolean>} - Успех операции
 */
async function copyToClipboard(text) {
    try {
        await navigator.clipboard.writeText(text);
        return true;
    } catch (err) {
        // Фоллбэк для старых браузеров
        const textArea = document.createElement('textarea');
        textArea.value = text;
        textArea.style.position = 'fixed';
        textArea.style.left = '-999999px';
        textArea.style.top = '-999999px';
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();

        try {
            document.execCommand('copy');
            document.body.removeChild(textArea);
            return true;
        } catch (err) {
            document.body.removeChild(textArea);
            return false;
        }
    }
}

/**
 * Дебаунс функция для оптимизации событий
 * @param {Function} func - Функция для выполнения
 * @param {number} wait - Задержка в мс
 * @returns {Function} - Дебаунс-обёртка
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Экспорт функций для глобального доступа (если нужно)
window.GeoGamesMedieval = {
    copyToClipboard,
    debounce
};

// ========================================
// Галерея сервера (БЕСКОНЕЧНАЯ ПРОКРУТКА)
// ========================================
let galleryIndex = 0;
let isTransitioning = false;
let autoScrollTimer;
let slideWidth = 0;

function initGallery() {
    const track = document.getElementById('galleryTrack');
    const slides = document.querySelectorAll('.gallery-slide');
    if (!track || slides.length === 0) return;

    // Вычисляем ширину слайда
    slideWidth = slides[0].offsetWidth + 24; // ширина + gap

    // Клонируем последние 3 слайда и добавляем В НАЧАЛО
    for (let i = slides.length - 3; i < slides.length; i++) {
        const clone = slides[i].cloneNode(true);
        clone.classList.add('clone-start');
        track.insertBefore(clone, track.firstChild);
    }

    // Клонируем первые 3 слайда и добавляем В КОНЕЦ
    for (let i = 0; i < 3; i++) {
        const clone = slides[i].cloneNode(true);
        clone.classList.add('clone-end');
        track.appendChild(clone);
    }

    // Теперь начинаем с позиции 3 (после начальных клонов)
    galleryIndex = 3;
    track.style.transform = `translateX(-${galleryIndex * slideWidth}px)`;

    const allSlides = document.querySelectorAll('.gallery-slide');

    // Глобальная функция для кнопок
    window.moveGallery = function(direction) {
        if (isTransitioning) return;

        galleryIndex += direction;
        track.style.transition = 'transform 0.5s ease-in-out';
        track.style.transform = `translateX(-${galleryIndex * slideWidth}px)`;
        isTransitioning = true;

        // Если дошли до конца (клоны в конце)
        if (galleryIndex >= slides.length + 3) {
            setTimeout(() => {
                track.style.transition = 'none';
                galleryIndex = 3; // Прыгаем к началу оригинальных слайдов
                track.style.transform = `translateX(-${galleryIndex * slideWidth}px)`;
                isTransitioning = false;
            }, 500);
        }
        // Если дошли до начала (клоны в начале)
        else if (galleryIndex < 3) {
            setTimeout(() => {
                track.style.transition = 'none';
                galleryIndex = slides.length; // Прыгаем к концу оригинальных слайдов
                track.style.transform = `translateX(-${galleryIndex * slideWidth}px)`;
                isTransitioning = false;
            }, 500);
        }
        else {
            setTimeout(() => { isTransitioning = false; }, 500);
        }
    };

    // Автопрокрутка
    function startAutoScroll() {
        autoScrollTimer = setInterval(() => window.moveGallery(1), 3000);
    }

    startAutoScroll();
    track.addEventListener('mouseenter', () => clearInterval(autoScrollTimer));
    track.addEventListener('mouseleave', startAutoScroll);

    // Lightbox
    window.openLightbox = function(idx) {
        const img = slides[idx].querySelector('img');
        const lightbox = document.getElementById('lightbox');
        const lightboxImg = document.getElementById('lightboxImg');
        if (lightbox && img) {
            lightboxImg.src = img.src;
            lightbox.classList.add('active');
            document.body.style.overflow = 'hidden';
        }
    };

    window.closeLightbox = function() {
        document.getElementById('lightbox').classList.remove('active');
        document.body.style.overflow = 'auto';
    };
}

// Закрытие по Escape
document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') window.closeLightbox();
});

// Запуск после загрузки DOM
document.addEventListener('DOMContentLoaded', initGallery);

// ========================================
// Console greeting (для разработчиков)
// ========================================
console.log('%c🏰 GeoGamesMedieval', 'font-family: "MedievalSharp", cursive; font-size: 20px; color: #d4af37;');
console.log('%cДобро пожаловать в код сервера!', 'color: #b0b0c0;');
console.log('%cРазработано с любовью к средневековью и Minecraft ⚔️', 'color: #707085;');