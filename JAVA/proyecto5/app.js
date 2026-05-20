/**
 * Clínica Dental Sonrisas Blancas - Lógica de Interactividad y Accesibilidad
 * Autor: Lead UX/UI Designer & Frontend Architect
 */

document.addEventListener('DOMContentLoaded', () => {
    
    // ==========================================================================
    // 1. GESTIÓN DEL MENÚ MÓVIL Y ACCESIBILIDAD (A11Y)
    // ==========================================================================
    const mobileToggle = document.querySelector('.mobile-nav-toggle');
    const mobileNavigation = document.getElementById('mobile-navigation');
    const mobileLinks = document.querySelectorAll('.mobile-nav-link');
    const body = document.body;

    /**
     * Alterna la visibilidad del menú móvil y gestiona los atributos ARIA
     */
    function toggleMobileMenu() {
        const isExpanded = mobileToggle.getAttribute('aria-expanded') === 'true';
        
        // Sincronizar estado
        mobileToggle.setAttribute('aria-expanded', !isExpanded);
        mobileNavigation.classList.toggle('open');
        mobileNavigation.setAttribute('aria-hidden', isExpanded);
        
        // Bloquear scroll del body para evitar comportamientos extraños detrás del menú
        if (!isExpanded) {
            body.style.overflow = 'hidden';
            // Foco al primer enlace del menú móvil tras abrir
            setTimeout(() => {
                mobileLinks[0].focus();
            }, 100);
            document.addEventListener('keydown', trapFocus);
        } else {
            body.style.overflow = '';
            mobileToggle.focus();
            document.removeEventListener('keydown', trapFocus);
        }
    }

    /**
     * Atrapa el foco de teclado dentro del modal del menú móvil (Keyboard Trap)
     * Requisito de accesibilidad WCAG 2.1
     */
    function trapFocus(e) {
        if (e.key !== 'Tab') return;

        const focusableElements = mobileNavigation.querySelectorAll('a, button');
        const firstElement = focusableElements[0];
        const lastElement = focusableElements[focusableElements.length - 1];

        if (e.shiftKey) { // Shift + Tab
            if (document.activeElement === firstElement) {
                lastElement.focus();
                e.preventDefault();
            }
        } else { // Tab
            if (document.activeElement === lastElement) {
                firstElement.focus();
                e.preventDefault();
            }
        }
    }

    mobileToggle.addEventListener('click', toggleMobileMenu);

    // Cerrar el menú al hacer clic en un enlace de navegación móvil
    mobileLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (mobileNavigation.classList.contains('open')) {
                toggleMobileMenu();
            }
        });
    });

    // Cerrar menú con la tecla Escape
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && mobileNavigation.classList.contains('open')) {
            toggleMobileMenu();
        }
    });


    // ==========================================================================
    // 2. LOGIC DE SCROLL: HEADER DINÁMICO Y BOTÓN "BACK TO TOP"
    // ==========================================================================
    const header = document.querySelector('.main-header');
    const backToTopBtn = document.getElementById('back-to-top');
    const scrollThreshold = 100;

    window.addEventListener('scroll', () => {
        const currentScroll = window.scrollY;

        // Cambiar estilo de la cabecera
        if (currentScroll > scrollThreshold) {
            header.classList.add('scrolled');
        } else {
            header.classList.remove('scrolled');
        }

        // Mostrar u ocultar botón de volver arriba
        if (currentScroll > 500) {
            backToTopBtn.classList.add('visible');
        } else {
            backToTopBtn.classList.remove('visible');
        }
    });

    // Acción volver arriba con foco limpio al inicio
    backToTopBtn.addEventListener('click', () => {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
        // Devolver el foco al skip link o el body para evitar que quede flotando
        document.querySelector('.skip-link').focus();
    });


    // ==========================================================================
    // 3. SELECCIÓN ACTIVA DE ENLACES DE NAV SEGÚN LA SECCIÓN VISIBLE
    // ==========================================================================
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');

    const sectionObserverOptions = {
        root: null,
        rootMargin: '-30% 0px -60% 0px', // Detecta la sección activa predominantemente en el centro
        threshold: 0
    };

    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${id}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, sectionObserverOptions);

    sections.forEach(section => {
        sectionObserver.observe(section);
    });


    // ==========================================================================
    // 4. ANIMACIÓN AL HACER SCROLL (INTERSECTION OBSERVER PARA REVEALS)
    // ==========================================================================
    const revealElements = document.querySelectorAll('.reveal');

    const revealObserverOptions = {
        root: null,
        rootMargin: '0px 0px -10% 0px', // Comienza la animación justo antes de entrar por completo
        threshold: 0.1
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                // Dejamos de observar una vez animado para mejorar el rendimiento
                observer.unobserve(entry.target);
            }
        });
    }, revealObserverOptions);

    revealElements.forEach(element => {
        revealObserver.observe(element);
    });


    // ==========================================================================
    // 5. VALIDACIÓN DEL FORMULARIO Y MODAL DE CONFIRMACIÓN
    // ==========================================================================
    const form = document.getElementById('appointment-form');
    const modal = document.getElementById('success-modal');
    const closeModalBtn = document.getElementById('close-modal-btn');
    const modalUserName = document.getElementById('modal-user-name');
    const modalBackdrop = modal.querySelector('.modal-backdrop');

    // Elementos de error específicos
    const errors = {
        name: document.getElementById('name-error'),
        phone: document.getElementById('phone-error'),
        email: document.getElementById('email-error'),
        service: document.getElementById('service-error'),
        consent: document.getElementById('consent-error')
    };

    /**
     * Valida de manera estricta el formulario según estándares HTML5 y accesibilidad
     */
    function validateForm() {
        let isValid = true;
        
        // Reset de clases e información de error
        Object.keys(errors).forEach(key => {
            errors[key].textContent = '';
            const input = form.elements[key];
            if (input) input.classList.remove('invalid');
        });

        // 1. Validar Nombre
        if (form.name.value.trim().length < 3) {
            errors.name.textContent = 'Por favor, introduzca su nombre completo (mínimo 3 caracteres).';
            form.name.classList.add('invalid');
            isValid = false;
        }

        // 2. Validar Teléfono (Patrón sencillo para España y códigos internacionales)
        const phoneRegex = /^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$/;
        if (!phoneRegex.test(form.phone.value.trim()) || form.phone.value.trim().length < 9) {
            errors.phone.textContent = 'Por favor, introduzca un número de teléfono válido (mínimo 9 dígitos).';
            form.phone.classList.add('invalid');
            isValid = false;
        }

        // 3. Validar Correo Electrónico
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(form.email.value.trim())) {
            errors.email.textContent = 'Por favor, introduzca una dirección de correo electrónico válida.';
            form.email.classList.add('invalid');
            isValid = false;
        }

        // 4. Validar Servicio
        if (!form.service.value) {
            errors.service.textContent = 'Por favor, seleccione el tratamiento o especialidad de su interés.';
            form.service.classList.add('invalid');
            isValid = false;
        }

        // 5. Validar Consentimiento LOPD/RGPD
        if (!form.consent.checked) {
            errors.consent.textContent = 'Es necesario aceptar el consentimiento de privacidad clínica para continuar.';
            isValid = false;
        }

        return isValid;
    }

    // Validación interactiva instantánea en cambio/blur para mejorar la experiencia de usuario
    ['name', 'phone', 'email', 'service', 'consent'].forEach(fieldKey => {
        const field = form.elements[fieldKey];
        if (field) {
            field.addEventListener('blur', () => {
                // Pequeña validación individual
                if (fieldKey === 'email') {
                    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                    if (!emailRegex.test(field.value.trim())) {
                        errors.email.textContent = 'Por favor, introduzca una dirección de correo electrónico válida.';
                        field.classList.add('invalid');
                    } else {
                        errors.email.textContent = '';
                        field.classList.remove('invalid');
                    }
                }
                if (fieldKey === 'name') {
                    if (field.value.trim().length >= 3) {
                        errors.name.textContent = '';
                        field.classList.remove('invalid');
                    }
                }
                if (fieldKey === 'phone') {
                    const phoneRegex = /^[5-9][0-9]{8}$|^[+][0-9]{11,15}$/; // Simplificado para móviles o formatos comunes
                    if (field.value.trim().length >= 9) {
                        errors.phone.textContent = '';
                        field.classList.remove('invalid');
                    }
                }
            });
        }
    });

    // Envío del Formulario
    form.addEventListener('submit', (e) => {
        e.preventDefault();

        if (validateForm()) {
            const submitBtn = form.querySelector('.btn-submit');
            submitBtn.classList.add('loading');
            submitBtn.setAttribute('disabled', 'true');

            // Simulación de envío API (Concierge Dental Integration)
            setTimeout(() => {
                submitBtn.classList.remove('loading');
                submitBtn.removeAttribute('disabled');

                // Abrir modal de éxito y personalizar nombre
                modalUserName.textContent = form.name.value.trim();
                openModal();
                
                // Limpiar formulario de manera segura
                form.reset();
            }, 1500);
        } else {
            // Foco al primer elemento inválido para mejorar la accesibilidad
            const firstInvalid = form.querySelector('.invalid');
            if (firstInvalid) {
                firstInvalid.focus();
            }
        }
    });

    /**
     * Gestión del Modal
     */
    function openModal() {
        modal.classList.add('open');
        modal.setAttribute('aria-hidden', 'false');
        body.style.overflow = 'hidden';
        closeModalBtn.focus();
        document.addEventListener('keydown', trapModalFocus);
    }

    function closeModal() {
        modal.classList.remove('open');
        modal.setAttribute('aria-hidden', 'true');
        body.style.overflow = '';
        document.removeEventListener('keydown', trapModalFocus);
        
        // Devolver el foco al botón de envío del formulario
        form.querySelector('.btn-submit').focus();
    }

    /**
     * Atrapa el foco de teclado en el modal de éxito (Keyboard Trap)
     */
    function trapModalFocus(e) {
        if (e.key === 'Escape') {
            closeModal();
            return;
        }
        if (e.key !== 'Tab') return;

        const focusable = modal.querySelectorAll('button');
        const first = focusable[0];
        const last = focusable[focusable.length - 1];

        if (e.shiftKey) {
            if (document.activeElement === first) {
                last.focus();
                e.preventDefault();
            }
        } else {
            if (document.activeElement === last) {
                first.focus();
                e.preventDefault();
            }
        }
    }

    closeModalBtn.addEventListener('click', closeModal);
    modalBackdrop.addEventListener('click', closeModal);

});
